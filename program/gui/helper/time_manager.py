import cv2
import pyaudio
import wave
import threading
import time
import subprocess
import os
import shutil

class VideoRecorder():  

	# Video class based on openCV 
	def __init__(self, filename):

		global this_student_folder
		self.open = True
		self.device_index = 0
		self.fps = 9               # fps should be the minimum constant rate at which the camera can
		self.fourcc = "MJPG"       # capture images (with no decrease in speed over time; testing is required)
		self.frameSize = (640,480) # video formats and sizes also depend and vary according to the camera used
		self.video_filename = str(os.path.join(this_student_folder, filename+".avi"))
		self.video_cap = cv2.VideoCapture(self.device_index, cv2.CAP_DSHOW)
		self.video_writer = cv2.VideoWriter_fourcc(*self.fourcc)
		self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
		self.frame_counts = 1
		self.start_time = time.time()


	# Video starts being recorded 
	def record(self):

		# counter = 1
		timer_start = time.time()
		# timer_current = 0


		while(self.open==True):
			ret, video_frame = self.video_cap.read()
			if (ret==True):

					self.video_out.write(video_frame)
					# print( str(counter) + " " + str(self.frame_counts) + " frames written " + str(timer_current) )
					self.frame_counts += 1
					# counter += 1
					# timer_current = time.time() - timer_start
					time.sleep(0.16)
					gray = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
					# cv2.imshow('video_frame', gray)
					cv2.waitKey(1)
			else:
				break

				# 0.16 delay -> 6 fps
				# 


	# Finishes the video recording therefore the thread too
	def stop(self):

		if self.open==True:

			self.open=False
			self.video_out.release()
			self.video_cap.release()
			cv2.destroyAllWindows()

		else: 
			pass


	# Launches the video recording function using a thread          
	def start(self):
		video_thread = threading.Thread(target=self.record)
		video_thread.start()





class AudioRecorder():


	# Audio class based on pyAudio and Wave
	def __init__(self, filename):

		self.open = True
		self.rate = 44100
		self.frames_per_buffer = 1024
		self.channels = 2
		self.format = pyaudio.paInt16
		self.audio_filename = str(os.path.join(this_student_folder, filename+".wav"))
		self.audio = pyaudio.PyAudio()
		self.stream = self.audio.open(format=self.format,
									  channels=self.channels,
									  rate=self.rate,
									  input=True,
									  frames_per_buffer = self.frames_per_buffer)
		self.audio_frames = []


	# Audio starts being recorded
	def record(self):

		self.stream.start_stream()
		while(self.open == True):
			data = self.stream.read(self.frames_per_buffer) 
			self.audio_frames.append(data)
			if self.open==False:
				break


	# Finishes the audio recording therefore the thread too    
	def stop(self):

		if self.open==True:
			self.open = False
			self.stream.stop_stream()
			self.stream.close()
			self.audio.terminate()

			waveFile = wave.open(self.audio_filename, 'wb')
			waveFile.setnchannels(self.channels)
			waveFile.setsampwidth(self.audio.get_sample_size(self.format))
			waveFile.setframerate(self.rate)
			waveFile.writeframes(b''.join(self.audio_frames))
			waveFile.close()

		pass

	# Launches the audio recording function using a thread
	def start(self):
		audio_thread = threading.Thread(target=self.record)
		audio_thread.start()





def start_AVrecording(filename):

	global video_thread
	global audio_thread

	video_thread = VideoRecorder(filename)
	audio_thread = AudioRecorder(filename)

	audio_thread.start()
	video_thread.start()

	return filename




def stop_AVrecording(filename):
	print( "active threads in time manager.py",threading.active_count() )


	audio_thread.stop() 
	frame_counts = video_thread.frame_counts
	elapsed_time = time.time() - video_thread.start_time
	recorded_fps = frame_counts / elapsed_time
	print( "total frames " + str(frame_counts) )
	print( "elapsed time " + str(elapsed_time) )
	print( "recorded fps " + str(recorded_fps) )
	video_thread.stop()

	# Makes sure the threads have finished

	while threading.active_count() > 3:
		time.sleep(1)




def this_student_directory_create(student_folder_directory_path):
	global this_student_folder

	# local_path = os.getcwd() #replace by os.path.realpath
	# parent_path = os.path.dirname(local_path)
	# data_folder = os.path.join( str(parent_path) ,"student_interview_data")
	this_student_directory =  os.path.join(student_folder_directory_path, this_student_folder)
	print("this_student_directory",this_student_directory)
	# check for student_interview_data folder

	if not os.path.exists( this_student_directory ):
		print("THIS student directory NOT found.. so creating STUDENT SPECIFIC FOLDER")
		os.mkdir(  this_student_directory )
	# print(os.path.exists(os.path.join(data_folder, this_student_folder) ))
	# print(os.path.join(data_folder, this_student_folder) )
	
	else:
		shutil.rmtree( this_student_directory )
		print("this student specifuc directory already existes so deleted")
		os.mkdir(this_student_directory )
	return  this_student_directory



def create_directory(student_folder):
	global this_student_folder
	this_student_folder = student_folder #this will be used by other functions
	local_path = os.path.realpath(__file__)
	parent_path = os.path.dirname( (os.path.dirname(local_path) ) )
	student_directory_path = os.path.join( str(parent_path) ,"student_interview_data" )

	# check for student_interview_data folder

	if not os.path.exists(student_directory_path ):
		print("No student directory file system found.. so creating")
		# print((os.path.join( str(parent_path) ,"student_interview_data") ))
		# print(os.getcwd())
		os.mkdir(student_directory_path )
		print(student_directory_path)
	else:
		print("\n student directory file system found \n")

		return student_directory_path

		# NO NEED TO DELETE IF ITS EXISTS




this_student_folder = ""


def run(filename, this_student_folder_directory_path, duration=15):
	global this_student_folder
	# this_student_directory_create(studentFolder)

	# # file_manager(filename)
	# local_path = os.getcwd()
	# parent_path = os.path.dirname(local_path)
	# all_student_data_folder = os.path.join( str( parent_path ), "student_interview_data")
	# this_student_folder = str(os.path.join( str(all_student_data_folder), studentFolder))
	
	this_student_folder = this_student_folder_directory_path
	
	start_AVrecording(filename)  
	time.sleep(duration)
	# while duration: 
	# 	mins, secs = divmod(duration, 60) 
	# 	timer = '{:02d}:{:02d}'.format(mins, secs) 
	# 	print(timer, end="\r") 
	# 	time.sleep(1) 
	# 	duration -= 1
		
	stop_AVrecording(filename)
	print ("\n Done \n")

# run("q1_read",3)