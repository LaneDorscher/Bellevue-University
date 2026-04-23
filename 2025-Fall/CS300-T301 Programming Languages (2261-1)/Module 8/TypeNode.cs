

class TypeNode
{
    public string Kind;
    public List<TypeNode> Children;
    public int Size;

    public TypeNode(string kind)
    {
        this.Kind = kind;
        Children = new List<TypeNode>();
        Size = -1;
    }

    public static bool TypeEqual(TypeNode t1, TypeNode t2, HashSet<(TypeNode, TypeNode)> visited = default)
    {
        visited ??= new HashSet<(TypeNode, TypeNode)>();

        var pair = (t1, t2);
        if (visited.Contains(pair)) return true;
        visited.Add(pair);

        if (t1.Kind != t2.Kind) return false; 
        if (t1.Kind == "array" && t1.Size != t2.Size) return false; 
        if (t1.Children.Count != t2.Children.Count) return false; 

        for (int i = 0;i < t1.Children.Count; i++)
            if (!TypeEqual(t1.Children[i], t2.Children[i], visited)) return false;
        
        return true;
    }

}