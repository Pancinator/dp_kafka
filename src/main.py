"""
Main class - running class
Starts processing of frames
"""


from dp_kafka.src.process_frames import ProcessFrames


def main():
    process_frames: ProcessFrames = ProcessFrames()
    process_frames.start_threads()


if __name__ == "__main__":
    main()
