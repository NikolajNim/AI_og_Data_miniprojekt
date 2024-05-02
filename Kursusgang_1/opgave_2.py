import os
import cv2
import pyaudio
import wave
import threading

class VideoRecorder:
    def __init__(self, duration):
        self.duration = duration
        self.frame_width = 640
        self.frame_height = 480
        self.fps = 20

    def record_video(self):
        file_path = os.path.join(os.getcwd() + "/Kursusgang_1/video_lyd_mappe/", "video.avi")
        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'XVID'), self.fps, (self.frame_width, self.frame_height))
        start_time = cv2.getTickCount()
        while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < self.duration:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("Kunne ikke optage frame.")
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print("Video gemt som", file_path)

class AudioRecorder:
    def __init__(self, duration):
        self.duration = duration
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024

    def record_audio(self):
        file_path = os.path.join(os.getcwd() + "/Kursusgang_1/video_lyd_mappe/", "audio.wav")
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk)
        frames = []
        start_time = cv2.getTickCount()
        while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < self.duration:
            data = stream.read(self.chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("Lyd gemt som", file_path)

def record_video_and_audio(duration):
    video_recorder = VideoRecorder(duration)
    audio_recorder = AudioRecorder(duration)

    video_thread = threading.Thread(target=video_recorder.record_video)
    audio_thread = threading.Thread(target=audio_recorder.record_audio)

    video_thread.start()
    audio_thread.start()

    video_thread.join()
    audio_thread.join()

# Optag video og lyd i 10 sekunder og gem dem i mappen video_lyd_mappe
record_video_and_audio(duration=10)
