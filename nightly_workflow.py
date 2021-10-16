from sparrow.version_ops import VersionControl

pkgname = "manim_kunyuan"
# vc = VersionControl(pkgname, "manimlib", version="0.27")
vc = VersionControl(pkgname, "manimlib")
# vc.update_version(1)
vc.update_readme(license="")
# vc.install()
vc.upload_pypi()