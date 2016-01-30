#slashUStr = "\\u0063\\u0072\\u0069\\u0066\\u0061\\u006E\\u0020\\u5728\\u8DEF\\u4E0A"; #crifan 在路上
slashUStr = "\u5df4\u8c46,\u96c4\u9ec4";
decodedUniChars = slashUStr.decode("unicode-escape")
print "decodedUniChars=",decodedUniChars; #decodedUniChars= crifan 在路上
