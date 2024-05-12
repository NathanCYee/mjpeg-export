# Export Video to MJpeg

A simple python script to convert a video file into the proprietary MJpeg format for the [Socket Programming Assignment 6: Video Streaming with RTSP and RTP](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/VideoStreaming_programming_lab_only.pdf) lab from Computer Networking: a Top Down Approach by Jim Kurose and Keith Ross. 

## Usage
After the prerequisites are installed, run the python file using the command:

```bash
python3 export.py /path/to/video /path/to/exported_file.Mjpeg num_frames
```

- The video file has to be in a format supported by your installed OpenCV version.
- num_frames is the distance in seconds between exported frames and can be a decimal value

## Prerequisites 
- python 3.7+
- opencv-python

opencv-python can be installed using the following commands depending on your python install type:

- Python 3:
```bash
pip3 install opencv-python
```
- Conda:
```bash
conda install opencv-python
```

## Limitations
- The video cannot be of a high resolution as each frame has to be encoded into 5 digits. If the size of the frame is larger than 99999 bytes, the script will drop the frame.
- Frames larger than approxmiately 9000 bytes will cause network drops because of UDP packet size limitations.

## License

BSD-3 Clause