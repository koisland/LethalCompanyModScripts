# Lethal Company mod scripts
Various scripts for Lethal Company modding

## Getting started
Install dependencies with `pixi`.
```bash
pixi install
```

## Usage

### `set_equal_custom_dungeon_wts`
Modifies a `LethalLevelLoader.cfg` so that custom dungeons have equal weights on all levels.
```bash
python src/set_level_loader_vals.py \
    -i test/LethalLevelLoader.cfg \
    -o test/ModLethalLevelLoader.cfg
```

Check diff with:
```bash
git diff --no-index test/LethalLevelLoader.cfg test/ModLethalLevelLoader.cfg
```

```diff
 ## Add this Dungeon to a Level's randomization pool based on matching Level Tags. (Minimum: 0, Maximum: 999999)
 # Setting type: String
@@ -155,7 +155,7 @@ Dungeon Injection Settings - Manual Mod Names List = Default Values Were Empty
 ## Add this Dungeon to a Level's randomization pool based on matching Level Names. (Minimum: 0, Maximum: 999999)
 # Setting type: String
 # Default value: Lua:300,Alacrity:300,Thrive:150,Hyx:9999999,Sorrow:900,Coralation:3000
-Dungeon Injection Settings - Manual Level Names List = Lua:300,Alacrity:300,Thrive:150,Hyx:9999999,Sorrow:900,Coralation:3000
+Dungeon Injection Settings - Manual Level Names List = Lua:9999999,Alacrity:9999999,Thrive:9999999,Hyx:9999999,Sorrow:9999999,Coralation:9999999
```
