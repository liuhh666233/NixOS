{
    description = "A demo project for NixOS and Nix and NixFlakes";
    
    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/21.05";
    };

    outputs = { self, nixpkgs}:
        let system = "x86_64-linux";
            pkgs = import nixpkgs {
                system = system;
            };
            customPython3 = pkgs.python3.withPackages (
                py-packages: [py-packages.click]
            );

        in {
            devShell."${system}" = pkgs.mkShell rec{
                name = "nixos-demo";
                buildInputs = with pkgs;[
                    customPython3
                ];
                shellHook = ''
                  export PS1="$(echo -e '\uf3e2') {\[$(tput sgr0)\]\[\033[38;5;228m\]\w\[$(tput sgr0)\]\[\033[38;5;15m\]} (${name}) \\$ \[$(tput sgr0)\]"
                '';
            };
            defaultPackage."${system}" = pkgs.python3Packages.callPackage ./default.nix {};
    
        };
}