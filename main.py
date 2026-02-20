import argparse
import sys

import interface


def search_and_connect_camera():
    print("Camera connected (initialize capture here)")


def calibrate():
    print("Calibration process here (e.g., select ROI)")


def run_monitor(config):
    print(f"Running monitoring with config: {config}")
    # Start the monitoring process, call capture, analyze, record


def launch_gui():
    interface.main()


def main():
    parser = argparse.ArgumentParser(description="Display Monitoring Tool")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("search-and-connect-camera", help="Search and connect to a camera")
    subparsers.add_parser("calibrate camera", help="Calibrate (e.g., set ROI)")

    run_parser = subparsers.add_parser("run", help="Start monitoring")
    run_parser.add_argument("--config", required=True, help="Path to configuration file")

    subparsers.add_parser("gui", help="Launch PyQt interface")

    args = parser.parse_args()

    if not args.command:
        launch_gui()
    elif args.command == "search-and-connect-camera":
        search_and_connect_camera()
    elif args.command == "calibrate camera":
        calibrate()
    elif args.command == "run":
        run_monitor(args.config)
    elif args.command == "gui":
        launch_gui()


if __name__ == "__main__":
    main()
