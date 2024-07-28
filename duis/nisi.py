try:
    # Some long-running operation or loop
    while True:
        print("Running...")
except KeyboardInterrupt:
    print("Keyboard interrupt received, exiting gracefully.")
    # Perform any necessary cleanup here
