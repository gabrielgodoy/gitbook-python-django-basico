from urllib import request


def openFile(url):
    response = request.urlopen(url)
    csv = response.read()
    dest_url = r'./sample.csv'
    file_write = open(dest_url, 'w')
    # Double backslash (\\) is to scape a backslash. We get one backlash only
    formatted_csv = str(csv).split('\\r\\n')
    for line in formatted_csv:
        file_write.write(line + '\n')
    file_write.close()


openFile('http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')
