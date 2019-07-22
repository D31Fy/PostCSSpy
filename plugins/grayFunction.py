def FindIn(row, start, end, n=None):
	m = n or len(start)
	RowStart = row.find(start) + m
	RowEnd   = row.find(end, RowStart)
	Result   = row[RowStart:RowEnd]

	return Result


def grayFunction(src, dist, FileName):
	InFileName = src + FileName 
	OutFileName = dist + FileName 

	FileIn = open(InFileName, 'r')
	Content = FileIn.read()
	FileIn.close()
	grayCount = str(Content).count('gray(')
	FileOut = open(OutFileName, 'w')
	FileOut.write(Content)
	FileOut.close()

	for i in range(grayCount):
		FileOut = open(OutFileName, 'r')
		Content = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		FileOut.write(Content)
		FileOut.close()
		grayFunction = FindIn(Content, "gray(", ")")
		blackFunction = FindIn(Content, "black(", ")")

		FileOut = open(OutFileName, 'r')
		FileContent = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		NewFileContent = str(FileContent).replace("gray(" + grayFunction + ")", '#' + grayFunction + grayFunction + grayFunction).replace("black(" + blackFunction + ")", 'rgba(0, 0, 0, ' + blackFunction + ')')

		FileOut.write(NewFileContent)
	
	FileOut.close()
