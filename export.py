import cv2
import os
import sys
import tempfile

VIDEO_PATH = os.path.abspath(sys.argv[1])
EXPORT_PATH = os.path.abspath(sys.argv[2])
FRAME_RATE = float(sys.argv[3])  # distance in seconds between frames

print(f"Converting {VIDEO_PATH} -> {EXPORT_PATH}")


def save_frame(video, sec, save_path):
    # move video to position
    video.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    # extract frame
    frame_present, image = video.read()
    if frame_present:
        # export to jpg file
        cv2.imwrite(save_path, image)
    return frame_present


with tempfile.TemporaryDirectory() as tmpdir:
    video_capture = cv2.VideoCapture(VIDEO_PATH)
    success_count = 0
    fail_count = 0
    with open(EXPORT_PATH, "wb") as agg_file:
        sec = 0
        count = 1
        success = True
        while success:
            # move video forward
            count += 1
            sec += FRAME_RATE
            sec = round(sec, 2)
            # grab JPEG frame from video
            save_path = os.path.join(tmpdir, f"image{count}.jpg")
            success = save_frame(video_capture, sec, save_path)
            # write frame to Mjpeg file
            if success:
                with open(save_path, "rb") as f:
                    data = f.read()
                    # ensure length can be encoded into 5 digits before writing frame
                    if len(data) <= 10**5:
                        length_str = "{:05d}".format(len(data)).encode()
                        agg_file.write(length_str)
                        agg_file.write(data)
                        success_count += 1
                    else:
                        print(
                            f"Skipping frame {count}, size cannot be encoded into 5 digits!"
                        )
                        fail_count += 1
    print("Conversion done!")
    print(f"Frames saved: {success_count}")
    print(f"Frames failed: {fail_count}")