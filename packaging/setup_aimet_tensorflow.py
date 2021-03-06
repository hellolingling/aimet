#==============================================================================
#  @@-COPYRIGHT-START-@@
#
#  Copyright (c) 2020, Qualcomm Innovation Center, Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  @@-COPYRIGHT-END-@@
#==============================================================================

""" Package generation file for aimet tensorflow package """

from setuptools import setup, find_packages, find_namespace_packages
import setup_cfg # pylint: disable=import-error

package_url_base = setup_cfg.remote_url + "/releases/download/" + str(setup_cfg.version)

common_dep_whl = package_url_base + "/AimetCommon-" + str(setup_cfg.version) + "-py3-none-any.whl"

# get all packages , discard build files etc.
packages_found = find_packages() + find_namespace_packages(exclude=['*bin', 'pyenv3*', 'build', 'dist', '*bin', '*x86*'])

setup(
    name='AimetTensorflow',
    version=str(setup_cfg.version),
    author='Qualcomm Innovation Center, Inc.',
    author_email='aimet@noreply.github.com',
    packages=packages_found,
    url=package_url_base,
    license='NOTICE.txt',
    description='AIMET',
    long_description=open('README.txt').read(),
    package_data={'aimet_tensorflow':['acceptance_tests/*.*']},
    install_requires=[],
    dependency_links=[common_dep_whl],
    include_package_data=True,
    zip_safe=True,
    platforms='x86',
    python_requires='>=3.6',
)
