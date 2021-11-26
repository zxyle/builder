package ${package.Mapper};

import ${package.Entity}.${entity};
import ${superMapperClassPackage};
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * ${table.comment!} Mapper 接口
 */
@Repository
public interface ${table.mapperName} extends ${superMapperClass}<${entity}> {

    List<${entity}> selectAll();

    // 截断表
    void truncate();

}
