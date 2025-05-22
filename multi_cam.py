import cv2
import numpy as np
import pykinect_azure as pykinect

window_title = "Infrared Image"
wait_key_time = 1

def main():
	while cv2.getWindowProperty(window_title, cv2.WND_PROP_VISIBLE) >= 1:
		#
		key_code = cv2.waitKey(wait_key_time)
		# Get capture
		capture1 = device1.update()
		capture2 = device2.update()
		# Get the infrared image
		ret, ir_image1 = capture1.get_ir_image()
		ret, ir_image2 = capture2.get_ir_image()
		#
		if not ret:
			continue
		#
		rendered_frame1 = ir_image1
		rendered_frame1 = cv2.resize(rendered_frame1, (500, 500))
		rendered_frame2 = ir_image2
		rendered_frame2 = cv2.resize(rendered_frame2, (500, 500))
		vertical_concat = np.concatenate((rendered_frame1, rendered_frame2), axis = 0)
		# Plot image
		cv2.imshow(window_title, vertical_concat)
		# Press q key to stop
		if (key_code & 0xFF) == ord('q'):
			device1.close()
			cv2.destroyAllWindows()
			break

if __name__ == "__main__":
	# Initialize the library, if the library is not found, add the library path as argument
	pykinect.initialize_libraries()
	# Modify camera configuration - master
	device_config1 = pykinect.default_configuration
	device_config1.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
	device_config1.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
	# Modify camera configuration - subordinate
	device_config2 = pykinect.default_configuration
	device_config2.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
	device_config2.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
	# Start device
	device1 = pykinect.start_device(config = device_config1)
	device2 = pykinect.start_device(config = device_config2)
	#
	cv2.namedWindow('Infrared Image',cv2.WINDOW_NORMAL)
	main()