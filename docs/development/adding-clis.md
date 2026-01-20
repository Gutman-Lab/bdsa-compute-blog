# Adding CLIs to BDSA

This guide explains how to build and add custom Command Line Interface (CLI) tools to BDSA (Digital Slide Archive / HistomicsUI). CLIs allow you to create custom analysis tools that integrate with the HistomicsUI analysis panel and have APIs automatically created for them.

## Overview

BDSA uses Docker-based CLIs that can be integrated into the HistomicsUI interface. Each CLI consists of:
- A Docker image containing the analysis code
- Python implementation file
- XML configuration file defining parameters
- Registration in `slicer_cli_list.json`

For reference, see the [slicer-cli-example repository](https://github.com/Gutman-Lab/slicer-cli-example) which provides a complete working example.

## Prerequisites

- Docker installed and configured
- Access to a BDSA/DSA instance (admin access recommended for development)
- Understanding of Python and XML

## Creating a New CLI

### Step 1: Set Up the Directory Structure

1. Create a new directory for your CLI in the `cli/` folder:
   ```bash
   mkdir -p cli/YourCLIName/
   ```

2. Create two files with the same name as your directory:
   - `YourCLIName.py` - Python implementation
   - `YourCLIName.xml` - XML configuration

### Step 2: Register the CLI

Add your CLI to `slicer_cli_list.json`:

```json
{
  "YourCLIName": {
    "type": "python"
  }
}
```

### Step 3: Create the XML Configuration File

The XML file defines the parameters, inputs, and outputs for your CLI. Follow the structure of existing CLIs (see `cli/PositivePixelCount/PositivePixelCount.xml` for reference).

Key sections in the XML file:
- **Parameters**: Define input parameters, thresholds, options
- **Inputs**: Specify input images, files, or data
- **Outputs**: Define output files, annotations, or results

Example structure:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<executable>
  <category>YourCategory</category>
  <title>Your CLI Title</title>
  <description>Description of what your CLI does</description>
  <version>0.1</version>
  <parameters>
    <!-- Define your parameters here -->
  </parameters>
</executable>
```

### Step 4: Implement the Python Code

The Python file contains your analysis logic. It uses the DSA's CLI parser class to read parameters defined in the XML file.

Key points:
- Use `CLIArgumentParser` to parse command-line arguments
- Parameters defined in XML are automatically available as arguments
- Access input files and paths through the parser
- Output results to specified output files

Example structure:
```python
from histomicstk.cli.utils import CLIArgumentParser

def main(args):
    """Main function for your CLI."""
    # Your analysis code here
    # Access parameters via args.parameter_name
    pass

if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())
```

### Step 5: Build the Docker Image

Build your Docker image:
```bash
docker build -t <image-name>:<tag> .
```

**Development Tip:** Build the Docker image on the same machine running the BDSA instance with only one worker handling tasks. This avoids needing to push to Docker Hub during development.

## Adding the CLI to Your BDSA Instance

### Step 1: Navigate to Slicer CLI Web Tasks

1. Log in to your BDSA instance as an admin user
2. Navigate to the **Tasks** collection
3. Open the **Slicer CLI Web Tasks** folder

### Step 2: Upload the Docker Image

1. Click the **CLI** button at the top of the folder
2. Enter your Docker image name and tag: `<image-name>:<tag>`
3. Submit to upload

**Note:** If developing on a different machine, push your image to Docker Hub first so workers can pull it.

### Step 3: Verify Installation

1. Check the admin job menu to see if the upload was successful
2. If it failed, inspect the error messages to diagnose issues
3. Once successful, your CLI should appear:
   - In the HistomicsUI analysis panel
   - In the DSA API documentation page

## Example: Positive Pixel Count CLI

The repository includes a modified version of the Positive Pixel Count CLI as a reference example:

- **Location**: `cli/PositivePixelCount/`
- **Files**: `PositivePixelCount.py`, `PositivePixelCount.xml`
- **Reference**: See this example when creating your own CLIs

## Best Practices

1. **Parameter Naming**: Use descriptive, consistent parameter names
2. **Error Handling**: Include proper error handling and validation
3. **Documentation**: Document parameters and expected inputs/outputs
4. **Testing**: Test your CLI locally before deploying
5. **Versioning**: Use semantic versioning for your CLI versions
6. **Dependencies**: Clearly document any required dependencies in your Dockerfile

## Troubleshooting

### Upload Fails
- Check Docker image name and tag are correct
- Verify the image exists and is accessible
- Check admin job menu for detailed error messages
- Ensure workers can access Docker Hub if image is hosted there

### CLI Doesn't Appear
- Verify `slicer_cli_list.json` includes your CLI
- Check that Python and XML files are correctly named
- Ensure Docker image was built successfully
- Restart workers if needed

### Parameters Not Working
- Verify parameter names in XML match those used in Python
- Check that parameter types are correctly defined
- Ensure CLIArgumentParser is being used correctly

## Additional Resources

- [HistomicsUI Slicer CLI Documentation](https://github.com/DigitalSlideArchive/HistomicsUI/blob/master/docs/slicer_cli_plugins.rst)
- [Example Repository](https://github.com/Gutman-Lab/slicer-cli-example)
- [Docker Documentation](https://docs.docker.com/)

## Future Enhancements

*More details and advanced topics will be added here as they are developed.*

---

**Note:** This documentation is based on the BDSA/DSA slicer-cli system. For the most up-to-date information, refer to the [HistomicsUI documentation](https://github.com/DigitalSlideArchive/HistomicsUI/blob/master/docs/slicer_cli_plugins.rst).
