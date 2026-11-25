# Starship Thingy Mabobs and Such, Standalone

A fork of [Starship Thingy Mabobs and Such](https://github.com/lsamman/Starship-Thingy-Mabobs-and-Such) without anything derived from Starship Expansion Project (SEP). SEP is not needed. Part names are the same as in the full mod: install **one or the other**, never both.

| | What is in it | Notes |
|---|---|---|
| **Starship HLS** | Core, two crew sections with interiors, awning cargo section, legs, pod covers, two elevators, solar arrays, crane frame, moving floors, tray, white depot | [docs/HLS.md](docs/HLS.md) |
| **ITS 2016** | Booster, ship, crew, cargo and tanker sections, grid fins, legs, solar fans, crane | [docs/ITS.md](docs/ITS.md) |
| **Others** | Cargo winch, steel depot nose, payload plate and fairing, Block 3 leg, crew access arm, ship QD arm | |

## Left out

SEP's parts and changes to them: the Block 3 crew noses, the expendable core, the bay-door HLS cargo section, the white docking hardware, the forward RCS on SEP's noses. Craft that use those will not load.

## Engines

There are no main engines here: put any you like on the engine nodes. The HLS landing thrusters are included. The ITS Raptor rings and vacuum Raptor are optional configs that appear only if SEP is installed; nothing of SEP's is included. The ITS craft in `Ships/VAB` use them.

## Needs

ModuleManager, B9PartSwitch, Community Resource Pack. Breaking Ground for the winch, crane, elevators, floors and tray; SimpleAdjustableFairings for the fairing; HabTechProps for the interiors; Resurfaced and Shabby for the HLS materials. Optional: Waterfall, StagedAnimation, FreeIva, Community Category Kit, CryoTanks, StarshipLaunchExpansion (the tower the arms fit).

## Build

`./build_all.sh` (Blender 3.6 with io_object_mu; Python with numpy and Pillow).

Not affiliated with or endorsed by SpaceX or NASA. Licence: [LICENSE](LICENSE).
