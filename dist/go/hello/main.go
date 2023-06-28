// Code samples that accompany the AWS blog post on jsii
package hello

import (
	"reflect"

	_jsii_ "github.com/aws/jsii-runtime-go/runtime"
)

func init() {
	_jsii_.RegisterStruct(
		"jsii-code-samples.ExtProps",
		reflect.TypeOf((*ExtProps)(nil)).Elem(),
	)
	_jsii_.RegisterClass(
		"jsii-code-samples.HelloWorld",
		reflect.TypeOf((*HelloWorld)(nil)).Elem(),
		[]_jsii_.Member{
			_jsii_.MemberMethod{JsiiMethod: "fibonacci", GoMethod: "Fibonacci"},
			_jsii_.MemberProperty{JsiiProperty: "opts", GoGetter: "Opts"},
			_jsii_.MemberMethod{JsiiMethod: "sayHello", GoMethod: "SayHello"},
		},
		func() interface{} {
			return &jsiiProxy_HelloWorld{}
		},
	)
	_jsii_.RegisterInterface(
		"jsii-code-samples.IInt",
		reflect.TypeOf((*IInt)(nil)).Elem(),
		[]_jsii_.Member{
			_jsii_.MemberMethod{JsiiMethod: "foo", GoMethod: "Foo"},
			_jsii_.MemberProperty{JsiiProperty: "immutableNum", GoGetter: "ImmutableNum"},
			_jsii_.MemberProperty{JsiiProperty: "mutableNum", GoGetter: "MutableNum"},
		},
		func() interface{} {
			return &jsiiProxy_IInt{}
		},
	)
	_jsii_.RegisterStruct(
		"jsii-code-samples.Props",
		reflect.TypeOf((*Props)(nil)).Elem(),
	)
}
