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
		capture = device.update()
		# Get the infrared image
		ret, ir_image = capture.get_ir_image()
		#
		if not ret:
			continue
		#
		rendered_frame = ir_image
		rendered_frame = cv2.resize(rendered_frame, (500, 500))
		# Plot image
		cv2.imshow(window_title, rendered_frame)
		# Press q key to stop
		if (key_code & 0xFF) == ord('q'):
			device.close()
			cv2.destroyAllWindows()
			break

if __name__ == "__main__":
	# Initialize the library, if the library is not found, add the library path as argument
	pykinect.initialize_libraries()
	# Modify camera configuration - master
	device_config = pykinect.default_configuration
	device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
	device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
	# Start device
	device = pykinect.start_device(config = device_config)
	#
	cv2.namedWindow('Infrared Image',cv2.WINDOW_NORMAL)
	main()