"""
Main class - running class
Starts processing of frames
"""

from process_frames.process_frames import ProcessFrames


def main():
    process_frames: ProcessFrames = ProcessFrames()
    process_frames.process()


if __name__ == "__main__":
    main()
