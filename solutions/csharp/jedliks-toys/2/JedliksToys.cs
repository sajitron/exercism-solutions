class RemoteControlCar
{
    private int distance;
    private int battery = 100;
    
    public static RemoteControlCar Buy() => new RemoteControlCar();

    public string DistanceDisplay() => $"Driven {distance} meters";

    public string BatteryDisplay() => battery < 1 ? "Battery empty" : $"Battery at {battery}%";

    public void Drive()
    {
        if (this.battery > 0)
        {
            this.battery -= 1;
            this.distance += 20;
        }
    }
}
