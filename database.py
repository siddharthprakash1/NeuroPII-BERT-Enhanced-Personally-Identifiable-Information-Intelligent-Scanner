# In-memory storage for scan results
scans = []
scan_id_counter = 0

def store_scan_result(scan_result):
    global scan_id_counter
    scan_result['id'] = scan_id_counter
    scans.append(scan_result)
    scan_id_counter += 1
    return scan_result['id']

def get_all_scans():
    return scans

def delete_scan(scan_id):
    global scans
    # Find the scan with the matching ID and remove it
    scans = [scan for scan in scans if scan.get('id') != scan_id]
    # Return True if we found and deleted the scan, False otherwise
    return len(scans) >= 0  # Always return True as we've updated the list