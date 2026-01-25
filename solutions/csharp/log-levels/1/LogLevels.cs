static class LogLine
{
    public static string Message(string logLine)
    {
        var indexOfColon = logLine.IndexOf(":");
        var message = logLine.Substring(indexOfColon + 1);
        return message.Trim();
    }

    public static string LogLevel(string logLine)            
    {
        var indexOfColon = logLine.IndexOf(":");
        var logLevel = logLine[1..(indexOfColon-1)];
		return logLevel.ToLower();
    }

    public static string Reformat(string logLine)
    {
        var message = Message(logLine);
        var logLevel = LogLevel(logLine);
        return $"{message} ({logLevel})";
    }
}
