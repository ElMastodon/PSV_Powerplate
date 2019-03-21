from TSL2561 import TSL2561

if __name__ == "__main__":
    tsl = TSL2561(debug=True)
    print(tsl.lux())
