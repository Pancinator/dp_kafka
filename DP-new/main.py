"""
Main class - running class
"""


from consumers.process_frames import ProcessFrames


def main():
    process_frames = ProcessFrames()
    process_frames.process()


if __name__ == "__main__":
    main()
