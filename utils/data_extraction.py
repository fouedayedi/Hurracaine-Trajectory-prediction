import csv
filename = '../Dataset/hurdat2-1851-2022-050423.txt'
csv_file = '../Dataset/Saved_files/hurricane_data.csv'

class HurricaneDataParser:
    def __init__(self, filename):
        self.filename = filename
        self.headers = []
        self.data_entries = []
    
    def process(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i]
                if line:
                    if len(line) > 20: 
                        header = self.process_header(line)
                        self.headers.append(header)
                        i += 1
                        for j in range(header["Best_Track_Entries"]):
                            data_entry = self.process_line(lines[i])
                            self.data_entries.append(data_entry)
                            i += 1
                    else:
                        i += 1

    def process_header(self, line):
        return {
            "Basin": line[0:2],
            "ATCF_Cyclone_Number": int(line[2:4]),
            "Year": int(line[4:8]),
            "Name": line[18:28],
            "Best_Track_Entries": int(line[33:36])
        }
    
    def process_line(self, line):
        return {
            "Year": int(line[0:4]),
            "Month": int(line[4:6]),
            "Day": int(line[6:8]),
            "Hours": int(line[10:12]),
            "Minutes": int(line[12:14]),
            "Record_Identifier": line[16],
            "Status": line[19:21],
            "Latitude": float(line[23:27]),
            "Hemisphere_Lat": line[27],
            "Longitude": float(line[30:35]),
            "Hemisphere_Long": line[35],
            "Max Sustained Wind": line[39:42],
            "34 kt Wind Radii NE": line[50:53],
            "34 kt Wind Radii SE": line[56:59],
            "34 kt Wind Radii SW": line[62:65],
            "34 kt Wind Radii NW": line[68:71],
            "50 kt Wind Radii NE": line[74:77],
            "50 kt Wind Radii SE": line[80:83],
            "50 kt Wind Radii SW": line[86:89],
            "50 kt Wind Radii NW": line[92:95],
            "64 kt Wind Radii NE": line[98:101],
            "64 kt Wind Radii SE": line[104:107],
            "64 kt Wind Radii SW": line[110:113],
            "64 kt Wind Radii NW": line[116:119],
            "Radius of Maximum Wind": line[122:125]
        }

    def get_headers(self):
        return self.headers

    def get_data_entries(self):
        return self.data_entries


parser = HurricaneDataParser(filename)
parser.process()

headers = parser.get_headers()
data_entries = parser.get_data_entries()

print(headers[:5])
print(len(data_entries))


with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = list(headers[0].keys()) + list(data_entries[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    data_index = 0
    for header in headers:
        for _ in range(header["Best_Track_Entries"]):  # for each trajectory data point of the hurricane
            writer.writerow({**header, **data_entries[data_index]})
            data_index += 1
