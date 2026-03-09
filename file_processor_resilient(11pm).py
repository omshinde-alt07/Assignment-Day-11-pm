import os
import csv
import json
import time
import traceback

folder = "csv_files"

report = {
    "files_processed": [],
    "files_failed": [],
    "error_details": {}
}

for file in os.listdir(folder):

    if not file.endswith(".csv"):
        continue

    path = os.path.join(folder, file)

    retries = 0

    while retries <= 3:
        try:
            total = 0
            count = 0

            with open(path) as f:
                reader = csv.reader(f)

                for row in reader:
                    for value in row:
                        total += float(value)
                        count += 1

            avg = total / count

            report["files_processed"].append({
                "file": file,
                "sum": total,
                "average": avg
            })

            print("Processed:", file)
            break

        except PermissionError:
            retries += 1
            print("Permission error, retrying...")
            time.sleep(1)

        except Exception as e:
            report["files_failed"].append(file)
            report["error_details"][file] = traceback.format_exc()
            print("Failed:", file)
            break


with open("processing_report.json", "w") as f:
    json.dump(report, f, indent=4)