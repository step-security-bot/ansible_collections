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

2. update the playbooks under provisioner in `molecule/default/molecule.yml`

```yaml
...
provisioner:
  name: ansible
  playbooks:
    create: ../substrate/multipass/create.yml
    destroy: ../substrate/multipass/destroy.yml
    prepare: ../substrate/multipass/prepare.yml
  inventory:
    links:
      hosts: ../inventory/
```

3. Ensure local changes don't get pushed to remote

```bash
git update-index --skip-worktree molecule/default/molecule.yml
```

> If you need to change something in `molecule/defualt/molecule.yml` undo with the below command

```bash
git update-index --no-skip-worktree molecule/default/molecule.yml
```

### macos (Apple silicon)

1. install [orbstack](https://docs.orbstack.dev/install)
