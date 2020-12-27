def do_keypress(img, center, row_keys_points):
	global s
	# this fuction presses a key and marks the pressed key with blue color
	for row in row_keys_points:
		arr1 = list(npy.int0(npy.array(center) >= npy.array(row[1])))            # center of the contour has greater value than the top left corner point of a key
		arr2 = list(npy.int0(npy.array(center) <= npy.array(row[2])))            # center of the contour has less value than the bottom right corner point of a key
		if arr1 == [1, 1] and arr2 == [1, 1]:
			if(row[0][0]=='$'):
				format_to_file()
				exit(0)
			gui.press(row[0])
			print(row[0][0])
			s+=row[0][0]
			cv2.fillConvexPoly(img, npy.array([npy.array(row[1]), \
												npy.array([row[1][0], row[2][1]]), \
												npy.array(row[2]), \
												npy.array([row[2][0], row[1][1]])]), \
												(255, 0, 0))
	return img

def main():
	row_keys_points = get_keys()
	new_area, old_area = 0, 0
	c, c2 = 0, 0                                    # c stores the number of iterations for calculating the difference b/w present area and previous area
													# c2 stores the number of iterations for calculating the difference b/w present center and previous center
	flag_keypress = False                            # if a key is pressed then this flag is True
	while True:
		img = cam.read()[1]
		img = cv2.flip(img, 1)

		imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(imgHSV, hsv_lower, hsv_upper)
		blur = cv2.medianBlur(mask, 15)
		blur = cv2.GaussianBlur(blur , (5,5), 0)
		thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
		contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]

		if len(contours) > 0:
			cnt = max(contours, key = cv2.contourArea)

			if cv2.contourArea(cnt) > 350:
				# draw a rectangle and a center
				rect = cv2.minAreaRect(cnt)
				center = list(rect[0])
				box = cv2.boxPoints(rect)
				box = npy.int0(box)
				cv2.circle(img, tuple(npy.int0(center)), 2, (0, 255, 0), 2)
				cv2.drawContours(img,[box],0,(0,0,255),2)

				# calculation of difference of area and center
				new_area = cv2.contourArea(cnt)
				new_center = npy.int0(center)
				if c == 0:
					old_area = new_area
				c += 1
				diff_area = 0
				if c > 3:                                # after every 3rd iteration difference of area is calculated
					diff_area = new_area - old_area
					c = 0
				if c2 == 0:
					old_center = new_center
				c2 += 1
				diff_center = npy.array([0, 0])
				if c2 > 5:                                # after every 5th iteration difference of center is claculated
					diff_center = new_center - old_center
					c2 = 0
				# setting some thresholds
				center_threshold = 10
				area_threshold = 200
				if abs(diff_center[0]) < center_threshold or abs(diff_center[1]) < center_threshold:
					if diff_area > area_threshold and flag_keypress == False:
						# time.sleep
						img = do_keypress(img, new_center, row_keys_points)
						flag_keypress = True
					elif diff_area < -(area_threshold) and flag_keypress == True:
						flag_keypress = False
			else:
				flag_keypress = False
		else:
			flag_keypress = False

		# displaying the keyboard
		for key in row_keys_points:
			cv2.putText(img, key[0], key[3], cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
			cv2.rectangle(img, key[1], key[2], (0, 0, 0), thickness = 3)

		cv2.imshow("img", img)

		if cv2.waitKey(1) == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()
main()
