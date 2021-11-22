package ${package.Mapper};

import ${package.Entity}.${entity};
import ${superMapperClassPackage};
import org.springframework.stereotype.Repository;

/**
 * ${table.comment!} Mapper 接口
 */
@Repository
public interface ${table.mapperName} extends ${superMapperClass}<${entity}> {

}
