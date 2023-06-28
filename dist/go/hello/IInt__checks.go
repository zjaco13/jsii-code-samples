//go:build !no_runtime_type_checking

package hello

import (
	"fmt"
)

func (j *jsiiProxy_IInt) validateSetMutableNumParameters(val *float64) error {
	if val == nil {
		return fmt.Errorf("parameter val is required, but nil was provided")
	}

	return nil
}

