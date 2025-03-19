import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python layeredge.py <command>")
        print("Commands: hello, version, help")
        return

    command = sys.argv[1]
    if command == "hello":
        print("Hello from LayerEdge CLI!")
    elif command == "version":
        print("LayerEdge CLI v1.0")
    elif command == "help":
        print("Available commands: hello, version, help")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
#!/usr/bin/env node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("Usage: node index.js <command>");
    console.log("Commands: hello, version, help");
    process.exit(1);
}

switch (args[0]) {
    case "hello":
        console.log("Hello from LayerEdge CLI!");
        break;
    case "version":
        console.log("LayerEdge CLI v1.0");
        break;
    case "help":
        console.log("Available commands: hello, version, help");
        break;
    default:
        console.log(`Unknown command: ${args[0]}`);
}
