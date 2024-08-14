# DePIN Ansible Collection

## installation

### macos

```bash
brew install pipx
```

### linux

```bash
apt install pipx
```

> https://pipx.pypa.io/stable/installation/

```bash
pipx install ansible-core
pipx inject ansible-core requests pyutils
pipx install ansible-lint
```

```bash
pipx install --include-deps molecule
```

## Molecule Setup

### linux/windows

> intel Macs can also use this method

1. install [multipass](https://multipass.run/install)

### macos

1. install [orbstack](https://docs.orbstack.dev/install)

    ```bash
      brew install orbstack
    ```

OR

1. install [UTM](https://mac.getutm.app/)

    ```bash
      brew install --cask utm
    ```

2. update the playbooks under provisioner in `molecule/default/molecule.yml`

    ```yaml
    ...
    provisioner:
      name: ansible
      playbooks:
        create: ../substrate/<name>/create.yml
        destroy: ../substrate/<name>/destroy.yml
        prepare: ../substrate/<name>/prepare.yml
      inventory:
        links:
          hosts: ../inventory/
    ```

3. install required ansible collections

    ```bash
      ansible-galaxy install -r requirements.yml
    ```

---

> If you need to change something in `molecule/defualt/molecule.yml` use the following command

```bash
  git update-index --no-skip-worktree molecule/default/molecule.yml
```