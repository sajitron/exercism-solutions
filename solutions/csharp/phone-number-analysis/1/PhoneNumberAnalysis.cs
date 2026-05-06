public static class PhoneNumber
{
    public static (bool IsNewYork, bool IsFake, string LocalNumber) Analyze(string phoneNumber)
    {
        string dialingCode = phoneNumber[0..3];
        string prefixCode = phoneNumber[4..7];
        string lastFour = phoneNumber[^4..];

        return (dialingCode == "212", prefixCode == "555", lastFour);
    }

    public static bool IsFake((bool IsNewYork, bool IsFake, string LocalNumber) phoneNumberInfo) => phoneNumberInfo.IsFake;
}
