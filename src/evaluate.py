#Import Library
from keras.models import model_from_json
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

class Evaluate:
	
	def run(filename):
		#Using only CPU
		config = tf.ConfigProto( device_count = {'GPU': 0} ) 
		sess = tf.Session(config=config) 
		set_session(sess)

		# load json and create model
		json_file = open('../model/model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		# load weights into new model
		loaded_model.load_weights('../model/model.h5')
		print("Loaded model from disk")
		 
		# evaluate loaded model on test data
		from keras.preprocessing import image
		import numpy as np
		test_image = image.load_img(filename, target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result = loaded_model.predict(test_image)
		if result[0][0] == 1:
			prediction = 'parang'
		else:
			prediction = 'kawung'
		print((prediction))
		
		return str(prediction)

if __name__ == '__main__':		
	#Using only CPU
	config = tf.ConfigProto( device_count = {'GPU': 0} ) 
	sess = tf.Session(config=config) 
	set_session(sess)

	# load json and create model
	json_file = open('../model/model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights('../model/model.h5')
	print("Loaded model from disk")
	 
	# evaluate loaded model on test data
	from keras.preprocessing import image
	import numpy as np
	test_image = image.load_img(filename, target_size = (64, 64))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = loaded_model.predict(test_image)
	if result[0][0] == 1:
		prediction = 'parang'
	else:
		prediction = 'kawung'
	print((prediction))