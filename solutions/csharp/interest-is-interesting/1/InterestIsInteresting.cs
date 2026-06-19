static class SavingsAccount
{
    public static float InterestRate(decimal balance)
    {
        if (balance < 0)
        {
            return (float)3.213;
        } else if (balance >= 0 && balance < 1000)
        {
            return (float)0.5;
        } else if (balance >= 1000 && balance < 5000)
        {
            return (float)1.621;
        } else if (balance >= 5000)
        {
            return (float)2.475;
        } else
        {
            return (float)0;
        }
    }

    public static decimal Interest(decimal balance) => (decimal)(InterestRate(balance)/100) * balance;
    
    public static decimal AnnualBalanceUpdate(decimal balance) => balance + Interest(balance);

    public static int YearsBeforeDesiredBalance(decimal balance, decimal targetBalance)
    {

        int yearCount = 0;

        if (balance >= targetBalance)
        {
            return yearCount;
        }

        do
        {
            yearCount++;
            balance = AnnualBalanceUpdate(balance);
        } while (balance < targetBalance);

        return yearCount;
    }
}
