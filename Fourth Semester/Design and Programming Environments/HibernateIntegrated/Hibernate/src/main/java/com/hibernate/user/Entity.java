package com.hibernate.user;

import java.io.Serializable;

public interface Entity<ID> extends Serializable {
    void setId(ID id);
    ID getId();
}
