import os
import time

def call_classifier():
	print('call classifier on ' + filename)


output = os.system("rsync -avz root@35.196.83.72:/home/hanqijing/video-poster/uploads/ uploads/")

print('Download the new video list...')
print(output)

foldername = 'uploads/'

def stamp(foldername, filename):
	with open(foldername + filename + '.finished','w') as f:
		f.write('this file is processed at ' + str(time.time()))  

# build a closed_list of finished video files 
# so we don't have the run the classifier on them
# again
finished_list = set()
for filename in os.listdir(foldername):
	if filename.endswith(".finished"): 
		finished_list.add(filename)

# For each file in the folder
# grab the file that have not been classified yet
# classify them
# then print a timestamp to show they are classified
# if we need to rerun the classifier on a processed video
# just delete the video_file_name.finished stamp file
# the video will be processed on next iteration
for filename in os.listdir(foldername):
    if filename.endswith(".mp4"): # run the program through all video files only
    	finished_stamp =  filename + '.finished'

    	# mtime = os.path.getmtime(foldername + filename)
    	# if float(time.time() - mtime) <= 500 and 
    	if finished_stamp not in finished_list:
    		# call vijay pipeline
    		call_classifier()
    		
    		# print a time stamp to show the file is processed
    		stamp(foldername, filename)
