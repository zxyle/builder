class Builder < Formula
  include Language::Python::Virtualenv

  desc "Quickly generate scaffolding projects"
  homepage "https://github.com/zxyle/builder"
  url "https://github.com/zxyle/builder/archive/refs/tags/v0.0.1.zip"
  sha256 "9da3976be38f9c64ebf41b007c6f2b43623b45b71a3d1c5c84f0edf1a788d80a"
  license "MIT"
  revision 3
  head "https://github.com/zxyle/builder.git"

  livecheck do
    url :stable
  end

  bottle do
    cellar :any
    sha256 "08525974a3404b234d7de572fea0f6095c3e6749df9fc192d571b1f815f00f3d" => :big_sur
    sha256 "f147a50464261bd34bd8af04390584badc4241e9d37ca54332fe7dac07e1d570" => :arm64_big_sur
    sha256 "94142a948bb19d5f80bf22d7c3aab0778ef48a0900ba1d8fd454fa070de31844" => :catalina
    sha256 "8cb911e8ce3f82f81c7fde523269118c9986d2524fb7f6b45137636c7b9c418c" => :mojave
  end

  depends_on "python@3.9"

  resource "Jinja2" do
    url "https://files.pythonhosted.org/packages/4f/e7/65300e6b32e69768ded990494809106f87da1d436418d5f1367ed3966fd7/Jinja2-2.11.3.tar.gz"
    sha256 "a6d58433de0ae800347cab1fa3043cebbabe8baa9d29e668f1c768cb87a333c6"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/6b/47/c14abc08432ab22dc18b9892252efaf005ab44066de871e72a38d6af464b/requests-2.25.1.tar.gz"
    sha256 "27973dd4a904a4f13b263a19c866c13b92a39ed1c964655f025f3f8d3d75b804"
  end

  def install
    virtualenv_install_with_resources
    # bash_completion.install "contrib/completion/bash/docker-compose"
    # zsh_completion.install "contrib/completion/zsh/_docker-compose"
  end

  test do
    system bin/"builder", "--help"
  end
end
