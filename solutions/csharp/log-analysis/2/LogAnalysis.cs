public static class LogAnalysis 
{
    public static string SubstringAfter(this string str, string delimetr)
    {
        var charIndex = str.IndexOf(delimetr) + delimetr.Length;
        return str.Substring(charIndex);
    }

    public static string SubstringBetween(this string str, string delimeter1, string delimeter2)
    {
        var firstDelimeterIndex = str.IndexOf(delimeter1) + delimeter1.Length;
        var secondDelimeterIndex = str.IndexOf(delimeter2, firstDelimeterIndex);
        var textLength = secondDelimeterIndex - firstDelimeterIndex;
        return str.Substring(firstDelimeterIndex, textLength);
    }
    
    public static string Message(this string str) => SubstringAfter(str, ": ");

    public static string LogLevel(this string str) => SubstringBetween(str, "[", "]");
}