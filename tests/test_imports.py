import pkgutil

from pytest_archon import archrule  # type: ignore[attr-defined]

import adapters


def test_core_cant_import_adapters() -> None:
    (
        archrule("core_imports")
        .match("core.**")
        .should_not_import("adapters.*")
        .check("core")
    )


def test_adapters_dont_import_each_other() -> None:
    adapter_modules = (
        module.name for module in pkgutil.iter_modules(adapters.__path__)
    )
    exclude = {"api": ["graphql.app"]}
    for adapter in adapter_modules:
        rule = (
            archrule(f"adapter_{adapter}")
            .match("adapters.*")
            .should_not_import("adapters.*")
            .may_import(f"adapters.{adapter}.*")
        )
        for may_import in exclude.get(adapter, []):
            rule = rule.may_import(f"adapters.{may_import}")

        rule.check(f"adapters.{adapter}")
