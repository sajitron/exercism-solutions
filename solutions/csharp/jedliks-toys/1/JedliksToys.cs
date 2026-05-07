class RemoteControlCar
{
    private int distance;
    private int battery = 100;
    
    public static RemoteControlCar Buy() => new RemoteControlCar();

    public string DistanceDisplay() => $"Driven {distance} meters";

    public string BatteryDisplay()
    {
        if (battery < 1)
        {
            return "Battery empty";
        } else 
        {
            return $"Battery at {battery}%";
        }
    }

    public void Drive()
    {
        distance = battery < 1 ? distance : distance + 20;
        battery = battery < 1 ? 0 : battery - 1;
    }
}
