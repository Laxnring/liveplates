from openalpr import Alpr
import cv2
import sys
import os
import time

cam = cv2.VideoCapture(1)
cv2.namedWindow("test")
time.sleep(1)

alpr = Alpr("eu", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
    
alpr.set_top_n(20)
#alpr.set_default_region("md")
i = 0
counter_nothing = 0
plates_list = []
confidences = []
while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    cv2.imwrite(str(i)+ ".jpg", frame)
    results = alpr.recognize_file(str(i)+".jpg")
    #for plate in results["results"]:
    #    if plate not in plates:
    #        plates.append(plate["plate"])
    #        confidences.append(plate["confidence"])
    #    print(confidences[plates.index(plate["plate"])])
    #   confidences[plates.index(plate["plate"])] = confidences[plates.index(plate["plate"])] + plate["confidence"]
    plates = results["results"]
    if len(plates) > 0:
        for candidate in plates[0]['candidates']:
            if candidate["plate"] not in plates_list:
                plates_list.append(candidate["plate"])
                confidences.append(candidate["confidence"])
                continue
            confidences[plates_list.index(candidate["plate"])] += candidate["confidence"]
    
    if (not plates):
        counter_nothing += 1
    else:
        counter_nothing = 0

    if (counter_nothing == 50):
        plates_list = []
        confidences = []
        counter_nothing = 0
    try:
        ind = confidences.index(max(confidences))
        print(str(plates_list[ind]) + " " + str(confidences[ind]))
    except:
        pass
    os.remove(str(i)+".jpg")
    #print(results)
    k = cv2.waitKey(1)
    i = i + 1

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()