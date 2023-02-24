# pcap-to-csv
This repository is used as a module to convert pcap files(Channel State Information data) into csv format

## Usage
* Put the pcap files in `data/pcap` and run `create_dataset.py`
```buildoutcfg
python create_dataset.py
```

* Deafualt setting
    1. **I/Q Complex number**, ~~Amplitute~~
    2. **All Subcarriers**, ~~Delete Null,Pilot~~
    3. **Add MAC address column to dataframe**
    4. **Add packet arrival time to dataframe**
  
      
* Settings can be changed in `csi/pcapTodf.py`
