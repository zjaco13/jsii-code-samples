'''
# jsii-code-samples [![NPM](https://img.shields.io/npm/v/jsii-code-samples)](https://www.npmjs.com/package/jsii-code-samples) [![PyPI](https://img.shields.io/pypi/v/aws-jsiisamples.jsii-code-samples)](https://pypi.org/project/aws-jsiisamples.jsii-code-samples/) [![Maven](https://img.shields.io/maven-central/v/software.aws.jsiisamples.jsii/jsii-code-samples)](https://search.maven.org/artifact/software.aws.jsiisamples.jsii/jsii-code-samples) [![NuGet](https://img.shields.io/nuget/v/AWSSamples.Jsii)](https://www.nuget.org/packages/AWSSamples.Jsii/)

> An example jsii package authored in TypeScript that gets published as GitHub packages for Node.js, Python, Java and dotnet.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *


class HelloWorld(metaclass=jsii.JSIIMeta, jsii_type="jsii-code-samples.HelloWorld"):
    def __init__(
        self,
        *,
        good_name: typing.Optional[builtins.bool] = None,
        name: builtins.str,
    ) -> None:
        '''
        :param good_name: 
        :param name: 
        '''
        props = ExtProps(good_name=good_name, name=name)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="fibonacci")
    def fibonacci(self, num: jsii.Number) -> jsii.Number:
        '''
        :param num: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e90b876a8f956565c004efb4e0d0ec7a190c6706b50a482cf990c4b6d569b6)
            check_type(argname="argument num", value=num, expected_type=type_hints["num"])
        return typing.cast(jsii.Number, jsii.invoke(self, "fibonacci", [num]))

    @jsii.member(jsii_name="sayHello")
    def say_hello(self, name: builtins.str) -> builtins.str:
        '''
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7b67614386d19aedfc3819956db2d56ecb24f5d1ab5e14c2c2ef433173f3b4f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.invoke(self, "sayHello", [name]))

    @builtins.property
    @jsii.member(jsii_name="opts")
    def opts(self) -> "ExtProps":
        return typing.cast("ExtProps", jsii.get(self, "opts"))


@jsii.interface(jsii_type="jsii-code-samples.IInt")
class IInt(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="immutableNum")
    def immutable_num(self) -> jsii.Number:
        ...

    @builtins.property
    @jsii.member(jsii_name="mutableNum")
    def mutable_num(self) -> jsii.Number:
        ...

    @mutable_num.setter
    def mutable_num(self, value: jsii.Number) -> None:
        ...

    @jsii.member(jsii_name="foo")
    def foo(self) -> builtins.str:
        ...


class _IIntProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-code-samples.IInt"

    @builtins.property
    @jsii.member(jsii_name="immutableNum")
    def immutable_num(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "immutableNum"))

    @builtins.property
    @jsii.member(jsii_name="mutableNum")
    def mutable_num(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mutableNum"))

    @mutable_num.setter
    def mutable_num(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9079686846f673d31271bc0cbae92eda4261b4bd8e6687ce0390467d2e9983d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableNum", value)

    @jsii.member(jsii_name="foo")
    def foo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "foo", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInt).__jsii_proxy_class__ = lambda : _IIntProxy


@jsii.data_type(
    jsii_type="jsii-code-samples.Props",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Props:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36971bc9c8cea25c8e1cce31b37e7b382e79a995e91a635cb6f8c102b0f669f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-code-samples.ExtProps",
    jsii_struct_bases=[Props],
    name_mapping={"name": "name", "good_name": "goodName"},
)
class ExtProps(Props):
    def __init__(
        self,
        *,
        name: builtins.str,
        good_name: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: 
        :param good_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2052bfe21f4a6d10d0955515374db6ea80728ebd21930422e25c71835c5b4cc8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument good_name", value=good_name, expected_type=type_hints["good_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if good_name is not None:
            self._values["good_name"] = good_name

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def good_name(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("good_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ExtProps",
    "HelloWorld",
    "IInt",
    "Props",
]

publication.publish()

def _typecheckingstub__a5e90b876a8f956565c004efb4e0d0ec7a190c6706b50a482cf990c4b6d569b6(
    num: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7b67614386d19aedfc3819956db2d56ecb24f5d1ab5e14c2c2ef433173f3b4f(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9079686846f673d31271bc0cbae92eda4261b4bd8e6687ce0390467d2e9983d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36971bc9c8cea25c8e1cce31b37e7b382e79a995e91a635cb6f8c102b0f669f(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2052bfe21f4a6d10d0955515374db6ea80728ebd21930422e25c71835c5b4cc8(
    *,
    name: builtins.str,
    good_name: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
