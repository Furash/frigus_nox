import re, zipfile, sys

manifest = 'blender_manifest.toml'
with open(manifest, 'r') as f:
    content = f.read()

match = re.search(r'^version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', content, re.MULTILINE)
if not match:
    print('ERROR: Could not find version in ' + manifest)
    sys.exit(1)

major, minor, patch = int(match.group(1)), int(match.group(2)), int(match.group(3))
new_patch = patch + 1
new_version = f'{major}.{minor}.{new_patch}'

content = re.sub(r'^(version\s*=\s*")(\d+\.\d+\.\d+)(")', rf'\g<1>{new_version}\3', content, count=1, flags=re.MULTILINE)
with open(manifest, 'w') as f:
    f.write(content)

zip_name = f'frigus_nox-{new_version}.zip'
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('Frigus_Nox.xml')
    zf.write(manifest)

print(f'Version bumped: {major}.{minor}.{patch} -> {new_version}')
print(f'Created: {zip_name}')
