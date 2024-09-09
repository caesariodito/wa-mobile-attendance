{
  description = "A very basic flake with a shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }: 
  flake-utils.lib.eachDefaultSystem (
    system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.default = pkgs.mkShell { 
        packages = with pkgs; [
          python3Full
          virtualenv
          python3Packages.tkinter
          python3Packages.pydevtool
        ]; 

        # buildInputs = with pkgs; [
        #   chromium
        # ];
      };
    }
  );
}