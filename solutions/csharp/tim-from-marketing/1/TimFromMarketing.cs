static class Badge
{
    public static string Print(int? id, string name, string? department) => $"{NormalizedId(id)}{name} - {NormalizedDept(department)}";

    private static string NormalizedId(int? id) => id != null ? $"[{id?.ToString()}] - " : "";

    private static string NormalizedDept(string? department) => department?.ToUpper() ?? "OWNER";
}
