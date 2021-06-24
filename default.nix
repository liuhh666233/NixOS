{buildPythonApplication, click, setuptools}:
    buildPythonApplication {
        pname = "demo-cpu-info";
        version = "1.0.0";

        src = ./.;

        propagatedBuildInputs = [
            click setuptools
        ];

    }
