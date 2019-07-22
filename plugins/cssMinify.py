def FindIn(row, start, end, n=None):
	m = n or len(start)
	RowStart = row.find(start) + m
	RowEnd   = row.find(end, RowStart)
	Result   = row[RowStart:RowEnd]

	return Result


def cssMinify(src, dist, FileName):
	InFileName = src + FileName 
	OutFileName = dist + FileName 

	FileIn = open(InFileName, 'r')
	Content = FileIn.read()
	FileIn.close()
	FileOut = open(OutFileName, 'w')
	FileOut.write(Content)
	FileOut.close()

	for i in range(1):
		FileOut = open(OutFileName, 'r')
		Content = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		FileOut.write(Content)
		FileOut.close()

		FileOut = open(OutFileName, 'r')
		FileContent = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		NewFileContent = str(FileContent).replace('\n', '').replace('  ', '').replace(';}', '}')

		FileOut.write(NewFileContent)
	
	FileOut.close()
