#!/usr/bin/env python3
# copy of https://github.com/pointhi/kicad-color-schemes/blob/master/create_repository.py
#
# CC0 1.0 Universal
#
# Statement of Purpose
#
# The laws of most jurisdictions throughout the world automatically confer
# exclusive Copyright and Related Rights (defined below) upon the creator and
# subsequent owner(s) (each and all, an "owner") of an original work of
# authorship and/or a database (each, a "Work").
#
# Certain owners wish to permanently relinquish those rights to a Work for the
# purpose of contributing to a commons of creative, cultural and scientific
# works ("Commons") that the public can reliably and without fear of later
# claims of infringement build upon, modify, incorporate in other works, reuse
# and redistribute as freely as possible in any form whatsoever and for any
# purposes, including without limitation commercial purposes. These owners may
# contribute to the Commons to promote the ideal of a free culture and the
# further production of creative, cultural and scientific works, or to gain
# reputation or greater distribution for their Work in part through the use and
# efforts of others.
#
# For these and/or other purposes and motivations, and without any expectation
# of additional consideration or compensation, the person associating CC0 with a
# Work (the "Affirmer"), to the extent that he or she is an owner of Copyright
# and Related Rights in the Work, voluntarily elects to apply CC0 to the Work
# and publicly distribute the Work under its terms, with knowledge of his or her
# Copyright and Related Rights in the Work and the meaning and intended legal
# effect of CC0 on those rights.
#
# 1. Copyright and Related Rights. A Work made available under CC0 may be
# protected by copyright and related or neighboring rights ("Copyright and
# Related Rights"). Copyright and Related Rights include, but are not limited
# to, the following:
#
#   i. the right to reproduce, adapt, distribute, perform, display, communicate,
#   and translate a Work;
#
#   ii. moral rights retained by the original author(s) and/or performer(s);
#
#   iii. publicity and privacy rights pertaining to a person's image or likeness
#   depicted in a Work;
#
#   iv. rights protecting against unfair competition in regards to a Work,
#   subject to the limitations in paragraph 4(a), below;
#
#   v. rights protecting the extraction, dissemination, use and reuse of data in
#   a Work;
#
#   vi. database rights (such as those arising under Directive 96/9/EC of the
#   European Parliament and of the Council of 11 March 1996 on the legal
#   protection of databases, and under any national implementation thereof,
#   including any amended or successor version of such directive); and
#
#   vii. other similar, equivalent or corresponding rights throughout the world
#   based on applicable law or treaty, and any national implementations thereof.
#
# 2. Waiver. To the greatest extent permitted by, but not in contravention of,
# applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
# unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
# and Related Rights and associated claims and causes of action, whether now
# known or unknown (including existing as well as future claims and causes of
# action), in the Work (i) in all territories worldwide, (ii) for the maximum
# duration provided by applicable law or treaty (including future time
# extensions), (iii) in any current or future medium and for any number of
# copies, and (iv) for any purpose whatsoever, including without limitation
# commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes
# the Waiver for the benefit of each member of the public at large and to the
# detriment of Affirmer's heirs and successors, fully intending that such Waiver
# shall not be subject to revocation, rescission, cancellation, termination, or
# any other legal or equitable action to disrupt the quiet enjoyment of the Work
# by the public as contemplated by Affirmer's express Statement of Purpose.
#
# 3. Public License Fallback. Should any part of the Waiver for any reason be
# judged legally invalid or ineffective under applicable law, then the Waiver
# shall be preserved to the maximum extent permitted taking into account
# Affirmer's express Statement of Purpose. In addition, to the extent the Waiver
# is so judged Affirmer hereby grants to each affected person a royalty-free,
# non transferable, non sublicensable, non exclusive, irrevocable and
# unconditional license to exercise Affirmer's Copyright and Related Rights in
# the Work (i) in all territories worldwide, (ii) for the maximum duration
# provided by applicable law or treaty (including future time extensions), (iii)
# in any current or future medium and for any number of copies, and (iv) for any
# purpose whatsoever, including without limitation commercial, advertising or
# promotional purposes (the "License"). The License shall be deemed effective as
# of the date CC0 was applied by Affirmer to the Work. Should any part of the
# License for any reason be judged legally invalid or ineffective under
# applicable law, such partial invalidity or ineffectiveness shall not
# invalidate the remainder of the License, and in such case Affirmer hereby
# affirms that he or she will not (i) exercise any of his or her remaining
# Copyright and Related Rights in the Work or (ii) assert any associated claims
# and causes of action with respect to the Work, in either case contrary to
# Affirmer's express Statement of Purpose.
#
# 4. Limitations and Disclaimers.
#
#   a. No trademark or patent rights held by Affirmer are waived, abandoned,
#   surrendered, licensed or otherwise affected by this document.
#
#   b. Affirmer offers the Work as-is and makes no representations or warranties
#   of any kind concerning the Work, express, implied, statutory or otherwise,
#   including without limitation warranties of title, merchantability, fitness
#   for a particular purpose, non infringement, or the absence of latent or
#   other defects, accuracy, or the present or absence of errors, whether or not
#   discoverable, all to the greatest extent permissible under applicable law.
#
#   c. Affirmer disclaims responsibility for clearing rights of other persons
#   that may apply to the Work or any use thereof, including without limitation
#   any person's Copyright and Related Rights in the Work. Further, Affirmer
#   disclaims responsibility for obtaining any necessary consents, permissions
#   or other rights required for any use of the Work.
#
#   d. Affirmer understands and acknowledges that Creative Commons is not a
#   party to this document and has no duty or obligation with respect to this
#   CC0 or use of the Work.
#
# For more information, please see
# <http://creativecommons.org/publicdomain/zero/1.0/>

import datetime
import hashlib
import json
import zipfile

from pathlib import Path
from zipfile import ZipFile

ROOT_PATH = Path(__file__).resolve().parent
PACKAGES_JSON_PATH = ROOT_PATH / "packages.json"
RESOURCES_PATH = ROOT_PATH / "resources.zip"
REPOSITORY_JSON_PATH = ROOT_PATH / "repository.json"
METADATA_FILEAME = "metadata.json"
ICON_FILENAME = "icon.png"

REPOSITORY_BASE_URI = "https://github.com/74th/kicad-highcontrast-monokai-theme/releases/download"
VERSION = "1.0.0"

READ_SIZE = 65536


def sha256_of_file(path):
    file_hash = hashlib.sha256()

    with path.open("rb") as f:
        data = f.read(READ_SIZE)
        while data:
            file_hash.update(data)
            data = f.read(READ_SIZE)

    return file_hash.hexdigest()


def create_pcm_from_color_scheme(path, resulting_file):
    with ZipFile(resulting_file, 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        for json_file in path.glob("*.json"):
            if json_file.name == METADATA_FILEAME:
                zip.write(json_file, json_file.name)
                continue
            zip.write(json_file, f"colors/{json_file.name}")

        icon_file = path / ICON_FILENAME
        if icon_file.exists():
            zip.write(icon_file, f"resources/{ICON_FILENAME}")


def install_size_of_zip(zip_path):
    install_size = 0
    with ZipFile(zip_path, 'r') as zip:
        for file in zip.filelist:
            install_size += zip.getinfo(file.filename).file_size
    return install_size


def create_and_get_pcm(path):
    metadata_path = path / METADATA_FILEAME
    if not metadata_path.exists():
        return

    print(f"* create schema for: {path}")

    with metadata_path.open("rb") as f:
        metadata_json = json.load(f)

    identifier = metadata_json["identifier"]

    for metadata_version in metadata_json["versions"]:
        version = metadata_version['version']
        pkg_name = f"{identifier}_v{version}_pcm.zip"
        pkg_path = path / pkg_name

        if not pkg_path.exists():
            # create new package as it does not exist yet (new version)
            print(f"  * create package: {pkg_path}")
            create_pcm_from_color_scheme(path, pkg_path)

        # fill in package data
        metadata_version['download_sha256'] = sha256_of_file(pkg_path)
        metadata_version['download_size'] = pkg_path.stat().st_size
        metadata_version['download_url'] = f"{REPOSITORY_BASE_URI}/v{version}/{pkg_name}"
        metadata_version['install_size'] = install_size_of_zip(pkg_path)

    return metadata_json


def write_packages_json(package_array):
    packages_data = {"packages": package_array}

    with PACKAGES_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(packages_data, f, indent=4)

def write_resources_zip():
    with ZipFile(RESOURCES_PATH, 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        for path in ROOT_PATH.iterdir():
            if not path.is_dir():
                continue

            metadata_path = path / METADATA_FILEAME
            icon_path = path / ICON_FILENAME
            if not metadata_path.exists() or not icon_path.exists():
                continue

            with metadata_path.open("r") as f:
                metadata_json = json.load(f)

            identifier = metadata_json["identifier"]

            zip.write(icon_path, f"{identifier}/{ICON_FILENAME}")


def write_repository_json():
    packages_json_sha256 = sha256_of_file(PACKAGES_JSON_PATH)
    packages_json_update_timestamp = int(PACKAGES_JSON_PATH.stat().st_mtime)
    packages_json_update_time_utc = datetime.datetime.fromtimestamp(packages_json_update_timestamp, tz=datetime.timezone.utc)

    repository_data = {
        "$schema": "https://go.kicad.org/pcm/schemas/v1#/definitions/Repository",
        "maintainer": {
            "contact": {
                "web": "https://github.com/74th/kicad-highcontrast-monokai-theme/"
            },
            "name": "Atsushi Morimoto (@74th)"
        },
        "name": "kicad high contrast monokai schema by @74th",
        "packages": {
            "sha256": packages_json_sha256,
            "update_time_utc": packages_json_update_time_utc.strftime("%Y-%m-%d %H:%M:%S"),
            "update_timestamp": packages_json_update_timestamp,
            "url": f"{REPOSITORY_BASE_URI}/v{VERSION}/packages.json"
        }
    }

    if RESOURCES_PATH.exists():
        resources_sha256 = sha256_of_file(RESOURCES_PATH)
        resources_update_timestamp = int(RESOURCES_PATH.stat().st_mtime)
        resources_update_time_utc = datetime.datetime.fromtimestamp(resources_update_timestamp, tz=datetime.timezone.utc)
        repository_data["resources"] = {
            "sha256": resources_sha256,
            "update_time_utc": resources_update_time_utc.strftime("%Y-%m-%d %H:%M:%S"),
            "update_timestamp": resources_update_timestamp,
            "url": f"{REPOSITORY_BASE_URI}/v{VERSION}/resources.zip"
        }

    with REPOSITORY_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(repository_data, f, indent=4)


if __name__ == "__main__":
    # create all package zip files and return the full schema of each one
    schemas = []
    for path in ROOT_PATH.iterdir():
        if path.is_dir():
            schema = create_and_get_pcm(path)
            if schema:
                schemas.append(schema)
    schemas = sorted(schemas, key=lambda d: d['identifier'])

    # write packages.json and repository.json
    write_packages_json(schemas)
    write_resources_zip()
    write_repository_json()
